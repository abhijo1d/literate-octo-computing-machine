import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev` : 'http://localhost:8000'}/api/activities/`;

  // Trigger: workflow check commit
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        setLoading(false);
        console.log('Fetched activities:', results);
        console.log('Endpoint:', endpoint);
      })
      .catch(err => {
        setLoading(false);
        console.error('Error fetching activities:', err);
      });
  }, [endpoint]);

  if (loading) return <div className="text-center">Loading activities...</div>;
  return (
    <div className="card shadow-sm mb-4">
      <div className="card-header d-flex align-items-center justify-content-between">
        <h2 className="h4 mb-0">Activities</h2>
        <button className="btn btn-outline-primary btn-sm" onClick={() => window.location.reload()}>Refresh</button>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Date</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((a, i) => (
                <tr key={a.id || i}>
                  <td>{i + 1}</td>
                  <td>{a.type}</td>
                  <td>{a.duration}</td>
                  <td>{a.date}</td>
                  <td>
                    <button className="btn btn-sm btn-info" onClick={() => setSelected(a)} data-bs-toggle="modal" data-bs-target="#activityModal">View</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal for activity details */}
      <div className="modal fade" id="activityModal" tabIndex="-1" aria-labelledby="activityModalLabel" aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="activityModalLabel">Activity Details</h5>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              {selected ? (
                <ul className="list-group">
                  <li className="list-group-item"><strong>Type:</strong> {selected.type}</li>
                  <li className="list-group-item"><strong>Duration:</strong> {selected.duration} min</li>
                  <li className="list-group-item"><strong>Date:</strong> {selected.date}</li>
                  <li className="list-group-item"><strong>User:</strong> {selected.user?.name || 'N/A'}</li>
                </ul>
              ) : <span>No activity selected.</span>}
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Activities;
